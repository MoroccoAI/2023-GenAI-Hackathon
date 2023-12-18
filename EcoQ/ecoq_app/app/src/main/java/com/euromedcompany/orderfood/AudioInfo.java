package com.euromedcompany.orderfood;
public class AudioInfo {
    private String audioName;
    private String duration;
    private String storagePath; // Add storage path or reference

    // Required default constructor for Firebase
    public AudioInfo() {
        // Default constructor required for calls to DataSnapshot.getValue(AudioInfo.class)
    }

    public AudioInfo(String audioName, String duration, String storagePath) {
        this.audioName = audioName;
        this.duration = duration;
        this.storagePath = storagePath;
    }

    public String getAudioName() {
        return audioName;
    }

    public String getDuration() {
        return duration;
    }

    public String getStoragePath() {
        return storagePath;
    }
}
