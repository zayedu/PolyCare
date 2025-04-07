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

export default function SymptomUploadScreen() {
  const [q1text, setq1Text] = useState("");
  const [q2text, setq2Text] = useState("");
  const [q3text, setq3Text] = useState("");
  const [q4text, setq4Text] = useState("");
  const [q5text, setq5Text] = useState("");

  const saveData = async () => {
    try {
      const response = await fetch("http://192.168.40.246:5000/", {
        method: "GET",
      }).then((response) => response.json());

      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  const sendData = async () => {
    const listOfSymptoms = [q1text, q2text, q3text, q4text, q5text];
    console.log(listOfSymptoms);

    try {
      await fetch("http://192.168.40.246:5000/SymptomUploadResults", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({ response: listOfSymptoms }),
      }).then((response) => {
        response.json();
        console.log(response);
      });
    } catch (error) {
      console.error(error);
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
          <ScrollView showsVerticalScrollIndicator={false}>
            <Text h3 style={styles.title}>
              Symptom Upload
            </Text>

            {/* Question 1 */}
            <Text style={styles.question}>
              Question 1: Have you noticed any irregularities in your menstrual
              cycle, such as infrequent periods, missed periods, or periods that
              are unusually heavy or light?
            </Text>
            <Input
              placeholder="Answer here..."
              placeholderTextColor="#aaa"
              inputStyle={styles.input}
              onChangeText={setq1Text}
              value={q1text}
            />

            {/* Question 2 */}
            <Text style={styles.question}>
              Question 2: Have you experienced excessive hair growth in areas
              such as your face, chest, back, or abdomen?
            </Text>
            <Input
              placeholder="Answer here..."
              placeholderTextColor="#aaa"
              inputStyle={styles.input}
              onChangeText={setq2Text}
              value={q2text}
            />

            {/* Question 3 */}
            <Text style={styles.question}>
              Question 3: Have you been struggling with persistent acne or
              unusually oily skin?
            </Text>
            <Input
              placeholder="Answer here..."
              placeholderTextColor="#aaa"
              inputStyle={styles.input}
              onChangeText={setq3Text}
              value={q3text}
            />

            {/* Question 4 */}
            <Text style={styles.question}>
              Question 4: Have you noticed unexplained weight gain or found it
              difficult to lose weight despite diet and exercise?
            </Text>
            <Input
              placeholder="Answer here..."
              placeholderTextColor="#aaa"
              inputStyle={styles.input}
              onChangeText={setq4Text}
              value={q4text}
            />

            {/* Question 5 */}
            <Text style={styles.question}>
              Question 5: Have you experienced hair thinning or hair loss,
              particularly on the scalp?
            </Text>
            <Input
              placeholder="Answer here..."
              placeholderTextColor="#aaa"
              inputStyle={styles.input}
              onChangeText={setq5Text}
              value={q5text}
            />

            {/* Submit Button */}
            <Button
              title="Submit Data"
              icon={{ name: "check-circle", type: "feather", color: "white" }}
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
  },
  overlay: {
    flex: 1,
    width: "100%",
    backgroundColor: "rgba(0,0,0,0.4)",
    padding: 20,
  },
  blurContainer: {
    borderRadius: 20,
    padding: 20,
  },
  title: {
    color: "white",
    fontSize: 26,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 20,
  },
  question: {
    color: "#E78EA9",
    fontSize: 10,
    fontWeight: "600",
    marginVertical: 8,
  },
  input: {
    color: "white",
  },
  button: {
    backgroundColor: "rgba(255,255,255,0.15)",
    borderRadius: 12,
    borderWidth: 1,
    borderColor: "white",
    paddingVertical: 12,
    marginTop: 20,
  },
  buttonContainer: {
    marginTop: 10,
  },
});
