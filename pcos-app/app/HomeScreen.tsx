import { View, Text, Button } from "react-native";

export default function HomeScreen( {navigation}: {navigation: any} ){
    return (
        <View style={{flex: 1, marginTop: 20, marginBottom: 20 }}>
            <Button title="Upload Symptom Results" onPress={() => navigation.navigate("Symptom Upload Page")} />
        </View>
    )
}