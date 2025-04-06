import * as React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import SymptomUploadScreen from "./SymptomUploadScreen";
import UltrasoundUploadScreen from "./UltrasoundUploadScreen";
import BloodUploadScreen from "./BloodUploadScreen";
import HomeScreen from "./HomeScreen";
import ResultsViewerScreen from "./ResultsViewerServiceScreen";

const Stack = createNativeStackNavigator();

export default function Index() {
  return (
    <Stack.Navigator
      initialRouteName="PCOS Home Page"
      screenOptions={{
        headerTransparent: true, // 👈 Transparent header
        headerTintColor: "white", // White icons
        headerTitle: "", // Turn text off completely
        headerTitleAlign: "center",
        headerTitleStyle: { fontWeight: "bold" },
        headerShadowVisible: true, // 👈 Removes border/shadow under header
      }}
    >
      <Stack.Screen
        name="PCOS Home Page"
        component={HomeScreen}
        options={{ title: "PCOS Home" }}
      />
      <Stack.Screen
        name="Symptom Upload Page"
        component={SymptomUploadScreen}
        options={{ title: "Symptom Upload" }}
      />
      <Stack.Screen
        name="Ultrasound Upload Page"
        component={UltrasoundUploadScreen}
        options={{ title: "Ultrasound Upload" }}
      />
      <Stack.Screen
        name="Blood Test Upload Page"
        component={BloodUploadScreen}
        options={{ title: "Blood Test Upload" }}
      />
      <Stack.Screen
        name="ResultsViewer"
        component={ResultsViewerScreen}
        options={{ title: "PCOS Results" }}
      />
    </Stack.Navigator>
  );
}
