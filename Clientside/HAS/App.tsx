// App.tsx

import React, { useState, useEffect } from 'react';
import { View, Text, ActivityIndicator } from 'react-native';
import { Button } from 'react-native-elements';
import styles from './AppStyles';  // import styles

const App: React.FC = () => {
  const [isLoading, setLoading] = useState(true);
  const [on, setOn] = useState(false);

  // replace this with the actual function to check server connection
  const checkServerConnection = (): Promise<void> => {
    return new Promise<void>(resolve => {
      setTimeout(() => {
        resolve();
      }, 2000); // mock a delay for demonstration
    });
  };
  
  useEffect(() => {
    checkServerConnection().then(() => setLoading(false));
  }, []);

  const toggleLight = () => {
    //Replace with actual IP of Raspberry Pi
    fetch('http://raspberrypi.local/lights', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        on: !on,
      }),
    });
    setOn(!on);
  };

  if (isLoading) {
    return (
      <View style={styles.loadingScreen}>
        <ActivityIndicator size="large" color="#9b59b6" />
        <Text style={styles.loadingText}>Establishing connection...</Text>
      </View>
    );
  }

  return (
    <View style={styles.homeScreen}>
      {Array.from({ length: 6 }).map((_, i) => (
        <Button
          key={i}
          onPress={toggleLight}
          title={on ? 'Turn off' : 'Turn on'}
          buttonStyle={styles.button}
        />
      ))}
    </View>
  );
};

export default App;
