import { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";

export default function SymptomUploadScreen(){
    const [q1text, setq1Text] = useState('');
    const [q2text, setq2Text] = useState('');
    const [q3text, setq3Text] = useState('');
    const [q4text, setq4Text] = useState('');
    const [q5text, setq5Text] = useState('');
    // const [text, setText] = useState('');

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
        const listOfSymptoms = [q1text, q2text, q3text, q4text, q5text]
        console.log(listOfSymptoms);
        
        try {
            await fetch(
                'http://127.0.0.1:5000/post', {
                    method: 'POST',
                    headers : {'Content-Type': 'application/json', Accept : 'application/json'},
                    body: JSON.stringify({response: listOfSymptoms}
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
            <Text>Question 1: Have you noticed any irregularities in your menstrual cycle, such as infrequent periods, missed periods, or periods that are unusually heavy or light?</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Answer here..."
                onChangeText={newTextq1 => setq1Text(newTextq1)}
                defaultValue={q1text}
            />
            <Text>Question 2: Have you experienced excessive hair growth in areas such as your face, chest, back, or abdomen?</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Answer here..."
                onChangeText={newTextq2 => setq2Text(newTextq2)}
                defaultValue={q2text}
            />
            <Text>Question 3: Have you been struggling with persistent acne or unusually oily skin?</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Answer here..."
                onChangeText={newTextq3 => setq3Text(newTextq3)}
                defaultValue={q3text}
            />
            <Text>Question 4: Have you noticed unexplained weight gain or found it difficult to lose weight despite diet and exercise?</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Answer here..."
                onChangeText={newTextq4 => setq4Text(newTextq4)}
                defaultValue={q4text}
            />
            <Text>Question 5: Hair Loss or Thinning**:  \n   *"Have you experienced hair thinning or hair loss, particularly on the scalp?</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Answer here..."
                onChangeText={newTextq5 => setq5Text(newTextq5)}
                defaultValue={q5text}
            />
            <Button title = "Submit Data" onPress={sendData}/>
        </View>
    )
}