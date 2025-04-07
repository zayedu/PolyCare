import React, { useState } from "react";
import {
  ScrollView,
  StyleSheet,
  ImageBackground,
  View,
  Alert,
} from "react-native";
import { Input, Button, Text } from "@rneui/themed";
import { BlurView } from "expo-blur";

export default function LoginScreen({ navigation }: { navigation: any }) {
  const [user, setUser] = useState("");
  const [password, setPassword] = useState("");

  const loginAttempt = async () => {
    const listOfCredentials = [user, password];
    try {
      const response = await fetch("http://192.168.40.246:5000/LoginAttempt", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({ incomingRequestCredentials: listOfCredentials }),
      }).then((response) => {
        response.json();
        console.log("Output", response.status);
        if (response.status === 200) {
          setTimeout(function callback() {
            navigation.navigate("PCOS Home Page");
          }, 3000);
        } else {
          Alert.alert("Login Failed", "Incorrect username or password.");
        }
      });
    } catch (error: any) {
      console.error(error);
      Alert.alert("Error", "Could not complete login attempt.");
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
              Login
            </Text>

            <Input
              placeholder="Username"
              placeholderTextColor="#aaa"
              label="User"
              labelStyle={styles.label}
              inputStyle={styles.input}
              onChangeText={(newUser) => setUser(newUser)}
              value={user}
            />

            <Input
              placeholder="Password"
              placeholderTextColor="#aaa"
              label="Password"
              labelStyle={styles.label}
              inputStyle={styles.input}
              onChangeText={(newPassword) => setPassword(newPassword)}
              value={password}
              secureTextEntry={true} // 👈 hide password input
            />

            <Button
              title="Login"
              icon={{ name: "log-in", type: "feather", color: "white" }}
              iconRight
              buttonStyle={styles.button}
              containerStyle={styles.buttonContainer}
              onPress={loginAttempt}
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
  label: {
    color: "#E78EA9",
    marginBottom: 5,
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
