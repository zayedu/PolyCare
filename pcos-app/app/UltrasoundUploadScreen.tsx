import React, { useState } from "react";
import { View, StyleSheet, Image, ImageBackground } from "react-native";
import { Text, Button } from "@rneui/themed";
import { BlurView } from "expo-blur";
import {
  launchImageLibrary,
  ImageLibraryOptions,
} from "react-native-image-picker";

export default function UltrasoundUploadScreen() {
  const [imageUri, setImageUri] = useState<string | null>(null);
  const [uploadResponse, setUploadResponse] = useState<string>("");

  const selectImage = () => {
    const options: ImageLibraryOptions = {
      mediaType: "photo" as const,
      quality: 1,
    };

    launchImageLibrary(options, (response) => {
      if (response.didCancel) {
        console.log("User cancelled image picker");
      } else if (response.errorCode) {
        console.log("ImagePicker Error:", response.errorMessage);
      } else if (response.assets && response.assets.length > 0) {
        const asset = response.assets[0];
        setImageUri(asset.uri ?? null);
      }
    });
  };

  const uploadImage = async () => {
    if (!imageUri) {
      console.log("No image selected");
      return;
    }

    try {
      const fileResponse = await fetch(imageUri);
      const blob = await fileResponse.blob();
      const uriParts = imageUri.split("/");
      const filename = uriParts[uriParts.length - 1];

      const formData = new FormData();
      formData.append("image", blob, filename);

      const response = await fetch(
        "http://127.0.0.1:5000/UltrasoundAnalyzer/UploadResults",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      if (response.ok) {
        setUploadResponse(`Success: ${data.response}`);
      } else {
        setUploadResponse(`Error: ${data.error}`);
      }
    } catch (error: any) {
      console.error("Upload error:", error);
      setUploadResponse(`Upload error: ${error.message || error}`);
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
            Upload Ultrasound
          </Text>

          <Button
            title="Select Image"
            icon={{ name: "image", type: "feather", color: "white" }}
            buttonStyle={styles.button}
            containerStyle={styles.buttonContainer}
            onPress={selectImage}
          />
          {imageUri && (
            <Image source={{ uri: imageUri }} style={styles.imagePreview} />
          )}
          <Button
            title="Upload Image"
            icon={{ name: "upload", type: "feather", color: "white" }}
            buttonStyle={[styles.button, { backgroundColor: "#C96A86" }]}
            containerStyle={styles.buttonContainer}
            onPress={uploadImage}
          />
          {uploadResponse !== "" && (
            <Text style={styles.responseText}>{uploadResponse}</Text>
          )}
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
  imagePreview: {
    width: 250,
    height: 250,
    borderRadius: 10,
    marginVertical: 20,
    borderWidth: 1,
    borderColor: "#E78EA9",
  },
  responseText: {
    color: "#E78EA9",
    marginTop: 20,
    fontSize: 16,
    textAlign: "center",
  },
});
