import React from "react";
import { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";

export default function LoginScreen({ navigation }: { navigation: any }) {
    const [user, setUser] = useState('');
    const [password, setPassword] = useState('');

  // Function to call the backend and navigate to the ResultsViewer screen.
  const loginAttempt = async () => {
    const listOfCredentials = [user, password]
    try {
      const response = await fetch("http://127.0.0.1:5000/LoginAttempt", {
        method: "POST",
        headers : {'Content-Type': 'application/json', Accept : 'application/json'},
        body: JSON.stringify({incomingRequestCredentials: listOfCredentials}
        ),
    })
    .then(response => {
        response.json()
        console.log("Output", response.status)
        if (response.status == 200 ){
            setTimeout(function callback(){
                navigation.navigate("PCOS Home Page")
            },3000);
        }
    })

    } catch (error: any) {
      console.error(error);
      Alert.alert("Error", "Error calculating likelihood.");
    }
  };

  return (
    <View style={{ flex: 1, marginTop: 5}}>
      <Text style={{borderTopWidth:5}}>Login</Text>
      <View style={{ marginBottom: 20, marginTop: 50}}>
        <Text style={{borderTopWidth:5}}>User</Text>
            <TextInput
                style={{height: 40, padding: 5,  borderTopWidth:1, borderBottomWidth:5, borderColor:'black', marginBottom:5}}
                placeholder="Answer here..."
                onChangeText={newUser => setUser(newUser)}
                defaultValue={user}
            />
      </View>
      <View style={{ marginBottom: 20, marginTop: 50}}>
        <Text style={{borderTopWidth:5}}>Password</Text>
            <TextInput
                style={{height: 40, padding: 5,  borderTopWidth:1, borderBottomWidth:5, borderColor:'black', marginBottom:5}}
                placeholder="Answer here..."
                onChangeText={newPassword => setPassword(newPassword)}
                defaultValue={password}
            />
      </View>
      <Button title = "Login" onPress={loginAttempt}/>
    </View>
  );
}