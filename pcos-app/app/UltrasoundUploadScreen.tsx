import React, { useState } from "react";
import { View, Text, Button, Image, StyleSheet } from "react-native";
import {
  launchImageLibrary,
  ImageLibraryOptions,
} from "react-native-image-picker";

export default function UltrasoundUploadScreen() {
  const [imageUri, setImageUri] = useState<string | null>(null);
  const [uploadResponse, setUploadResponse] = useState<string>("");

  const selectImage = () => {
    const options: ImageLibraryOptions = {
      mediaType: "photo" as const, // Ensures mediaType is the literal "photo"
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
      // Fetch the local file and convert it to a Blob
      const fileResponse = await fetch(imageUri);
      const blob = await fileResponse.blob();

      // Extract filename from the URI
      const uriParts = imageUri.split("/");
      const filename = uriParts[uriParts.length - 1];

      const formData = new FormData();
      // Append the Blob to FormData (do not set headers manually)
      formData.append("image", blob, filename);

      // Send the request to the Flask backend
      const response = await fetch(
        "http://127.0.0.1:5000/UltrasoundAnalyzer/UploadResults",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      if (response.ok) {
        setUploadResponse(
          `Success: ${data.response} (Status: ${response.status})`
        );
      } else {
        setUploadResponse(`Error: ${data.error} (Status: ${response.status})`);
      }
      console.log("Upload response:", data);
    } catch (error: any) {
      console.error("Upload error:", error);
      setUploadResponse(`Upload error: ${error.message || error}`);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Upload Ultrasound Image</Text>
      <Button title="Select Image" onPress={selectImage} />
      {imageUri && (
        <Image source={{ uri: imageUri }} style={styles.imagePreview} />
      )}
      <Button title="Upload Image" onPress={uploadImage} />
      {uploadResponse !== "" && (
        <Text style={styles.responseText}>{uploadResponse}</Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  imagePreview: {
    width: 200,
    height: 200,
    marginVertical: 20,
  },
  responseText: {
    marginTop: 20,
    fontSize: 16,
  },
});
