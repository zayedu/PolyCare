import { useState } from "react";
import {
  ScrollView,
  StyleSheet,
  ImageBackground,
  View,
  Alert,
} from "react-native";
import { Input, Button, Text } from "@rneui/themed";
import { BlurView } from "expo-blur";

export default function BloodUploadScreen() {
  const [glucose, setGlucose] = useState("");
  const [testosterone, setTestosterone] = useState("");
  const [bileSalts, setBileSalts] = useState("");

  const sendData = async () => {
    console.log(glucose, testosterone, bileSalts);

    try {
      await fetch("http://127.0.0.1:5000/BloodTestUploadResults", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          glucose: parseFloat(glucose),
          testosterone: parseFloat(testosterone),
          bileSalts: parseFloat(bileSalts),
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          Alert.alert("Success", "Blood Test Results Submitted!");
        });
    } catch (error) {
      console.error(error);
      Alert.alert("Error", "Failed to submit blood test results.");
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
            Blood Test Upload
          </Text>

          <ScrollView showsVerticalScrollIndicator={false}>
            <Input
              placeholder="Glucose Levels (mmol/L)"
              label="Glucose"
              labelStyle={styles.label}
              inputStyle={styles.input}
              keyboardType="numeric"
              onChangeText={setGlucose}
              value={glucose}
            />
            <Input
              placeholder="Testosterone Levels (ng/dL)"
              label="Testosterone"
              labelStyle={styles.label}
              inputStyle={styles.input}
              keyboardType="numeric"
              onChangeText={setTestosterone}
              value={testosterone}
            />
            <Input
              placeholder="Bile Salt Levels (mmol/L)"
              label="Bile Salts"
              labelStyle={styles.label}
              inputStyle={styles.input}
              keyboardType="numeric"
              onChangeText={setBileSalts}
              value={bileSalts}
            />

            <Button
              title="Submit Blood Test"
              icon={{ name: "flask", type: "font-awesome-5", color: "white" }}
              iconRight
              buttonStyle={styles.button}
              containerStyle={styles.buttonContainer}
              onPress={sendData}
            />
          </ScrollView>
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
  blurContainer: { borderRadius: 20, padding: 20 },
  title: {
    color: "white",
    fontSize: 26,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
  },
  label: { color: "#C96A86", marginBottom: 5 },
  input: { color: "white" },
  button: {
    backgroundColor: "rgba(255,255,255,0.15)",
    borderRadius: 12,
    borderWidth: 1,
    borderColor: "white",
    marginTop: 20,
  },
  buttonContainer: { marginTop: 10 },
});
