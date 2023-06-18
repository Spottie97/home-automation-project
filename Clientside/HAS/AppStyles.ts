// AppStyles.ts

import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  loadingScreen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#2c3e50',
  },
  loadingText: {
    marginTop: 10,
    color: '#ecf0f1',
  },
  homeScreen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ecf0f1',
  },
  button: {
    margin: 20,
    backgroundColor: '#9b59b6',
    borderRadius: 10,
  },
});

export default styles;
