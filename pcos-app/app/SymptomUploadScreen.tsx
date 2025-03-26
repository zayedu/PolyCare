import { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";

export default function SymptomUploadScreen(){
    const [text, setText] = useState('');

    const saveData = async ()=>{
        
        try {
            const response = await fetch(
              'http://127.0.0.1:5000/', {method: 'GET'}
            ).then(response=> response.json());
            
            console.log(response)
        } catch (error) {
            console.error(error);
        }
    };

    const sendData = async ()=>{
        console.log(text);
        
        try {
            await fetch(
                'http://127.0.0.1:5000/post', {
                    method: 'POST',
                    headers : {'Content-Type': 'application/json', Accept : 'application/json'},
                    body: JSON.stringify({response: text}
                    ),
                })
                .then(response => {
                    response.json()
                })
        }
        catch (error) {
            console.error(error);
        }
    };

    return (
        <View >
            <Text>SymptomUpload</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Input..."
                onChangeText={newText => setText(newText)}
                defaultValue={text}
            />
            <Button title = "Submit Data" onPress={sendData}/>
        </View>
    )
}