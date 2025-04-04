import * as React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import SymptomUploadScreen from "./SymptomUploadScreen";
import UltrasoundUploadScreen from "./UltrasoundUploadScreen";
import BloodUploadScreen from './BloodUploadScreen';
import HomeScreen from "./HomeScreen";
import ResultsViewerScreen from "./ResultsViewerServiceScreen";

const Stack = createNativeStackNavigator();

export default function Index() {
  return (
    <Stack.Navigator initialRouteName="PCOS Home Page">
      <Stack.Screen
        name="PCOS Home Page"
        options={{ headerTitleAlign: "center" }}
        component={HomeScreen}
      />
      <Stack.Screen
        name="Symptom Upload Page"
        options={{ headerTitleAlign: "center" }}
        component={SymptomUploadScreen}
      />
      <Stack.Screen
        name="Ultrasound Upload Page"
        options={{ headerTitleAlign: "center" }}
        component={UltrasoundUploadScreen}
      />
      <Stack.Screen
        name="Blood Test Upload Page"
        options={{ headerTitleAlign: "center" }}
        component={BloodUploadScreen}
      />
        <Stack.Screen
          name="ResultsViewer"
          component={ResultsViewerScreen}
        />
    </Stack.Navigator>
  );
}
