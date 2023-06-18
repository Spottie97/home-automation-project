// AppStyles.ts

import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  darkLoadingScreen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#2c3e50',
  },
  lightLoadingScreen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ecf0f1',
  },
  darkHomeScreen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#2c3e50',
  },
  lightHomeScreen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ecf0f1',
  },
  button: {
    backgroundColor: '#9b59b6',
    borderRadius: 25,
    height: 100,
    justifyContent: 'center',
    margin: 10,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  buttonText: {
    color: 'white',
    fontSize: 20,
    fontWeight: 'bold',
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-evenly',
    marginBottom: 10,
  },
  darkModeToggle: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'flex-end', // aligns the switch to the left
    margin: 10,
  },
  darkModeText: {
    color: 'white',
    marginRight: 10,
  },
  lightModeText: {
    color: 'black',
    marginRight: 10,
  },
  loadingText: {
    marginTop: 10,
    color: '#ecf0f1',
  },
});

export default styles;
