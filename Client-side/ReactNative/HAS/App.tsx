import React, { useState } from 'react';
import { Button, View } from 'react-native';

export default function App() {
  const [on, setOn] = useState(false);

  const toggleLight = () => {
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

  return (
    <View>
      <Button onPress={toggleLight} title={on ? 'Turn off' : 'Turn on'} />
    </View>
  );
}
