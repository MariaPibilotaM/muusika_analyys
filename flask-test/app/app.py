#Teekide importimine
import sys
import subprocess
import os
import time
import json

from flask import Flask, jsonify, request
from flask_cors import CORS

import numpy as np
from numpy import median, diff

import essentia
import essentia.standard as es

import tensorflow

import numba
import librosa

import pytube


musicnn_metadata = json.load(open('msd-musicnn-1.json', 'r'))

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

data = {}

#Essentia teegi abil tempo, helistiku ja tagg sõnade leidmine
def find_features(audio_path, name):
    features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                              rhythmStats=['mean', 'stdev'],
                                              tonalStats=['mean', 'stdev'])(audio_path)
    bpm = features['rhythm.bpm']
    helistik = (features['tonal.chords_key'], features['tonal.chords_scale'])
    energy = features['tonal.tuning_nontempered_energy_ratio']
    dance = features['rhythm.danceability'] / 3 #väärtuste vahemik on 0-3
    
    #JSON salvestamine
    data["nimi"] = name
    data['bpm'] = round(bpm)
    
    helilaad = 'minoor'
    if(helistik[1] != 'minor'):       
        helilaad = "mažoor"

    data["helistik"] = {"nimi": helistik[0],
                        "helilaad": helilaad}
    data["energia"] = round(energy,2) * 100
    data["tantsulisus"] = round(dance,2) * 100
    
    #TAGG SÕNAD
    sr = 16000
    audio = es.MonoLoader(filename=audio_path, sampleRate=sr)()

    musicnn_preds = es.TensorflowPredictMusiCNN(graphFilename='msd-musicnn-1.pb')(audio)

    classes = musicnn_metadata['classes']
        
    keskmised = np.mean(musicnn_preds.T, axis=1)
    valitud = []
    for i, l in enumerate(keskmised.argsort()[-4:][::-1], 1):
        valitud.append(classes[l])
    
    data['taggs'] = [{
            "tag": valitud[0]
        },{
            "tag": valitud[1]
        },{
            "tag": valitud[2]
        },{
            "tag": valitud[3]
          }]
        
def tempo_change(y,sr):
    # Eemaldame vaikuse
    yt, index = librosa.effects.trim(y)
    
    onset_env = librosa.onset.onset_strength(yt, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    dtempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, aggregate=None)
    
    lenght_of_the_song = librosa.get_duration(yt,sr)
    section = round(len(dtempo)/4)

    a = np.average(dtempo[:section])
    b = np.average(dtempo[section:(section*2)])
    c = np.average(dtempo[section*2:section*3])
    d = np.average(dtempo[section*3:])
    
    
    data["a"] = a
    data["b"] = b
    data["c"] = c
    data["d"] = d
    
def culmination(x, sr):
    lenght_of_the_song = librosa.get_duration(x,sr)

    S, phase = librosa.magphase(librosa.stft(x)) # compute magnitude and phase content
    rms = librosa.feature.rms(S=S)[0] # compute root-mean-square for each frame in magnitude

    rms_lenght = len(rms)

    #How much is one sec in this scale
    sec = round(rms_lenght/lenght_of_the_song)

    #Remembering best energy rms and index
    best = -1000900
    index = -1

    #Remembering sum and if we have collected data for 1 sec
    sum = 0
    at = 1
    #Only starting at 1/3 of the song
    for i in range(round(rms_lenght/3),rms_lenght):
      sum += rms[i]
      if(at == sec):
        if(sum> best):
          best = sum
          index = i
        at = 0
        sum = 0
      at += 1

    m, s = divmod(round(lenght_of_the_song/rms_lenght*index), 60)
    m_start, s_start = divmod(round(lenght_of_the_song/rms_lenght*index)-10, 60)
    data["kulminatsioon"] = {"a_m": m_start,
                             "a_s":s_start,
                             "l_m":m,
                             "l_s":s}
    
    
def find_tempo_features(audio_path):

    #Tempo muutus
    y, sr = librosa.load(audio_path)
    
    tempo_change(y, sr)
    culmination(y, sr)
    
@app.route('/data', methods=['GET', 'POST','DELETE'])
def get_data():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        if(request.form.get('link') != '-'):
            post_data = request.form.get('link')
            if not os.path.exists('songs'):
                os.makedirs('songs')
            pytube.YouTube(post_data).streams.filter(only_audio=True).first().download("songs/")
            entry = os.listdir('songs/')
            
            find_features('songs/'+ entry[0],entry[0])
            find_tempo_features('songs/'+ entry[0])
            
            os.remove('songs/'+ entry[0])

        else:
            f = request.files['file']
            f.save(f.filename)
            find_features('./'+f.filename,f.filename)
            find_tempo_features('./'+f.filename)
                
            os.remove('./'+f.filename)
        

        
    if request.method == 'DELETE':
        data.clear()
        response_object['message'] = 'Data cleared!'
    else:
        response_object['data'] = data
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)