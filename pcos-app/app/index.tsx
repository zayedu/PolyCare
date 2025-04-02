import * as React from 'react';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import SymptomUploadScreen from './SymptomUploadScreen';
import HomeScreen from './HomeScreen';
import BloodUploadScreen from './BloodUploadScreen';

const Stack = createNativeStackNavigator();

export default function Index() {
  
  return (
      <Stack.Navigator initialRouteName="PCOS Home Page"
        >
        <Stack.Screen
          name="PCOS Home Page"
          options={{headerTitleAlign: 'center'}}
          component={HomeScreen}
        />
        <Stack.Screen
          name="Symptom Upload Page"
          options={{headerTitleAlign: 'center'}}
          component={SymptomUploadScreen}
        />
        <Stack.Screen
          name="BloodUpload"
          options={{headerTitleAlign: 'center'}}
          component={BloodUploadScreen}
        />
      </Stack.Navigator>
  );
}
