import { View, Text, Button } from "react-native";

<<<<<<< HEAD
export default function HomeScreen( {navigation}: {navigation: any} ){
    return (
        <View >
            <Text>Home Screen</Text>
            <Button title="Upload Symptom Results" onPress={() => navigation.navigate("SymptomUpload")} />
            <Button title="Upload Blood Test Results" onPress = {() => navigation.navigate("BloodUpload")} />
        </View>
    )
}
=======
export default function HomeScreen({ navigation }: { navigation: any }) {
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
    </View>
  );
}
>>>>>>> main
