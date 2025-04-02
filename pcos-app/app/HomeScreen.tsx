import { View, Text, Button } from "react-native";

export default function HomeScreen( {navigation}: {navigation: any} ){
    return (
        <View >
            <Text>Home Screen</Text>
            <Button title="Upload Symptom Results" onPress={() => navigation.navigate("SymptomUpload")} />
            <Button title="Upload Blood Test Results" onPress = {() => navigation.navigate("BloodUpload")} />
        </View>
    )
}