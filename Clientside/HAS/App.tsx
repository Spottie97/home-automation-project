import React, {useState, useEffect} from 'react';
import {View, Text, ActivityIndicator, Switch} from 'react-native';
import {Button} from 'react-native-elements';
import styles from './AppStyles';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import {enableScreens} from 'react-native-screens';
import {SafeAreaProvider} from 'react-native-safe-area-context';

const Stack = createStackNavigator();
enableScreens();

const App: React.FC = () => {
  const [isLoading, setLoading] = useState(true);
  const [on, setOn] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const checkServerConnection = async (): Promise<void> => {
    try {
      const response = await fetch('http://<your_server_ip>:5000', {
        method: 'GET',
      });

      if (!response.ok) {
        throw new Error('Server not reachable');
      }

      setLoading(false);
    } catch (error) {
      // Handle or display the error as needed
      console.log(error);
    }
  };

  useEffect(() => {
    checkServerConnection();
  }, []);

  const toggleLight = async () => {
    try {
      const response = await fetch('http://<your_server_ip>:5000/lights', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          on: !on,
        }),
      });

      if (!response.ok) {
        throw new Error('Error in light toggling');
      }

      setOn(!on);
    } catch (error) {
      // Handle or display the error as needed
      console.log(error);
    }
  };

  if (isLoading) {
    return (
      <View
        style={
          isDarkMode ? styles.darkLoadingScreen : styles.lightLoadingScreen
        }>
        <ActivityIndicator
          size="large"
          color={isDarkMode ? '#ecf0f1' : '#9b59b6'}
        />
        <Text style={styles.loadingText}>Establishing connection...</Text>
      </View>
    );
  }

  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home">
            {({navigation}) => (
              <View
                style={
                  isDarkMode ? styles.darkHomeScreen : styles.lightHomeScreen
                }>
                <View style={styles.darkModeToggle}>
                  <Text
                    style={
                      isDarkMode ? styles.darkModeText : styles.lightModeText
                    }>
                    Dark Mode
                  </Text>
                  <Switch
                    trackColor={{false: '#767577', true: '#81b0ff'}}
                    thumbColor={isDarkMode ? '#f5dd4b' : '#f4f3f4'}
                    ios_backgroundColor="#3e3e3e"
                    onValueChange={() => setIsDarkMode(!isDarkMode)}
                    value={isDarkMode}
                  />
                </View>
                {Array.from({length: 3}).map((_, i) => (
                  <View key={i} style={styles.buttonRow}>
                    <Button
                      onPress={() => navigation.navigate('Details')}
                      buttonStyle={styles.button}
                      title="Go to Details"
                      titleStyle={styles.buttonText}
                    />
                    <Button
                      onPress={toggleLight}
                      buttonStyle={styles.button}
                      title={on ? 'Turn off' : 'Turn on'}
                      titleStyle={styles.buttonText}
                    />
                  </View>
                ))}
              </View>
            )}
          </Stack.Screen>
          <Stack.Screen name="Details">
            {({navigation}) => (
              <View
                style={
                  isDarkMode ? styles.darkHomeScreen : styles.lightHomeScreen
                }>
                {Array.from({length: 4}).map((_, i) => (
                  <View key={i} style={styles.buttonRow}>
                    <Button
                      onPress={toggleLight}
                      buttonStyle={styles.button}
                      title={on ? 'Turn off' : 'Turn on'}
                      titleStyle={styles.buttonText}
                    />
                  </View>
                ))}
              </View>
            )}
          </Stack.Screen>
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
};

export default App;
