import React from "react";
import { View, Button, Alert } from "react-native";

export default function HomeScreen({ navigation }: { navigation: any }) {
  // Function to call the backend and navigate to the ResultsViewer screen.
  const handleGetLikelihood = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/calculateLikelihood", {
        method: "POST",
      });
      const json = await response.json();
      if (json.success) {
        navigation.navigate("ResultsViewer");
      } else {
        Alert.alert("Error", "Failed to calculate likelihood.");
      }
    } catch (error: any) {
      console.error(error);
      Alert.alert("Error", "Error calculating likelihood.");
    }
  };

  return (
    <View style={{ flex: 1, marginTop: 20, marginBottom: 20 }}>
      <Button
        title="Upload Symptom Results"
        onPress={() => navigation.navigate("Symptom Upload Page")}
      />
      <Button
        title="Upload Ultrasound"
        onPress={() => navigation.navigate("Ultrasound Upload Page")}
      />
      <Button
        title="Upload Blood Test Results"
        onPress={() => navigation.navigate("Blood Test Upload Page")}
      />
      <Button
        title="Get My Likelihood"
        onPress={handleGetLikelihood}
        color="#C96A86" // Using the Dark Variant color for the button
      />
    </View>
  );
}