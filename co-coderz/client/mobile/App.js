import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TouchableHighlight, Linking } from 'react-native';

export default function App() {
  const [button1Pressed, setButton1Pressed] = useState(false);
  const [button2Pressed, setButton2Pressed] = useState(false);

  const redirectToBetaPage = () => {
    Linking.openURL('https://hyprsol.com/beta');
  };

  const redirectToYouTube = () => {
    Linking.openURL('https://youtu.be/NBixYx5mOe8');
  };

  return (
    <View style={styles.container}>
      <Image source={require('./assets/logo-wide-cropped.png')} style={styles.logo} resizeMode="contain" />
      <View style={styles.progressBarContainer}>
        {/* Assuming you want a fixed progress bar without a timer */}
        <View
          style={{
            height: 20,
            width: '50%', // Set your desired initial progress
            backgroundColor: 'pink', // Use your desired color
          }}
        />
      </View>
      <View style={styles.buttonContainer}>
        <TouchableHighlight
          style={[
            styles.button,
            { backgroundColor: button1Pressed ? '#800080' : 'pink' }, // Purple when pressed, pink otherwise
          ]}
          onPress={redirectToBetaPage}
          onHideUnderlay={() => setButton1Pressed(false)}
          onShowUnderlay={() => setButton1Pressed(true)}
        >
          <Text style={styles.buttonText}>Try Beta</Text>
        </TouchableHighlight>
        <TouchableHighlight
          style={[
            styles.button,
            { backgroundColor: button2Pressed ? '#800080' : 'pink' }, // Purple when pressed, pink otherwise
          ]}
          onPress={redirectToYouTube}
          onHideUnderlay={() => setButton2Pressed(false)}
          onShowUnderlay={() => setButton2Pressed(true)}
        >
          <Text style={styles.buttonText}>Learn More</Text>
        </TouchableHighlight>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#6a0572', // Dark violet background color
    alignItems: 'center',
    justifyContent: 'center',
  },
  logo: {
    height: 100,
    width: 200,
  },
  progressBarContainer: {
    marginTop: 20,
  },
  buttonContainer: {
    flexDirection: 'row', // Arrange buttons horizontally
    marginTop: 20,
  },
  button: {
    marginHorizontal: 8, // Adjust the spacing between buttons
    padding: 10,
    borderRadius: 8,
  },
  buttonText: {
    textAlign: 'center',
    color: 'black', // Set the text color to white
  },
});
