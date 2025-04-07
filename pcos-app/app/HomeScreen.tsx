import React from "react";
import { StyleSheet, ImageBackground, View } from "react-native";
import { Button, Text } from "@rneui/themed";
import { BlurView } from "expo-blur";

export default function HomeScreen({ navigation }: { navigation: any }) {
  const handleGetLikelihood = async () => {
    try {
      const response = await fetch(
        "http://192.168.40.246:5000/api/calculateLikelihood",
        {
          method: "POST",
        }
      );
      const json = await response.json();
      if (json.success) {
        navigation.navigate("ResultsViewer");
      } else {
        alert("Failed to calculate likelihood.");
      }
    } catch (error) {
      console.error(error);
      alert("Error calculating likelihood.");
    }
  };

  return (
    <ImageBackground
      source={require("../assets/images/background.jpg")}
      style={styles.background}
      resizeMode="cover"
    >
      <View style={styles.overlay}>
        <BlurView intensity={60} tint="dark" style={styles.blurContainer}>
          <Text h3 style={styles.title}>
            PCOS Home
          </Text>

          <Button
            title="Upload Symptom Results"
            icon={{
              name: "clipboard-list",
              type: "font-awesome-5",
              color: "white",
              size: 20,
            }}
            iconRight
            buttonStyle={styles.button}
            containerStyle={styles.buttonContainer}
            onPress={() => navigation.navigate("Symptom Upload Page")}
          />
          <Button
            title="Upload Blood Test Results"
            icon={{
              name: "flask",
              type: "font-awesome-5",
              color: "white",
              size: 20,
            }}
            iconRight
            buttonStyle={styles.button}
            containerStyle={styles.buttonContainer}
            onPress={() => navigation.navigate("Blood Test Upload Page")}
          />
          <Button
            title="Upload Ultrasound"
            icon={{ name: "image", type: "feather", color: "white", size: 20 }}
            iconRight
            buttonStyle={styles.button}
            containerStyle={styles.buttonContainer}
            onPress={() => navigation.navigate("Ultrasound Upload Page")}
          />
          <Button
            title="Get My Likelihood"
            icon={{
              name: "activity",
              type: "feather",
              color: "white",
              size: 20,
            }}
            iconRight
            buttonStyle={[styles.button, { backgroundColor: "#C96A86" }]}
            containerStyle={styles.buttonContainer}
            onPress={handleGetLikelihood}
          />
        </BlurView>
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    width: "100%",
    height: "100%",
    justifyContent: "center",
    alignItems: "center",
  },
  overlay: {
    flex: 1,
    width: "100%",
    backgroundColor: "rgba(0,0,0,0.4)",
    padding: 20,
  },
  blurContainer: { borderRadius: 20, padding: 20, alignItems: "center" },
  title: { color: "white", fontSize: 26, fontWeight: "bold", marginBottom: 20 },
  button: {
    backgroundColor: "rgba(255,255,255,0.15)",
    borderRadius: 12,
    borderWidth: 1,
    borderColor: "white",
    paddingVertical: 12,
    paddingHorizontal: 20,
  },
  buttonContainer: { width: "100%", marginVertical: 10 },
});
