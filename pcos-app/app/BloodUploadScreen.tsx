import { useState } from "react";
import { View, Text, TextInput, Button, Alert } from "react-native";

export default function BloodUploadScreen(){
    const [glucose, setGlucose] = useState('');
    const [testosterone, setTestosterone] = useState('');
    const [bileSalts, setBileSalts] = useState('');


    const sendData = async ()=>{
        console.log(glucose, testosterone, bileSalts);
        
        try {
            await fetch(
                'http://127.0.0.1:5000/BloodTestUploadResults', {
                    method: 'POST',
                    headers : {'Content-Type': 'application/json', Accept : 'application/json'},
                    body: JSON.stringify({glucose: parseFloat(glucose), testosterone: parseFloat(testosterone), bileSalts: parseFloat(bileSalts)}
                    ),
                })
                .then(response => response.json())
                .then(data=> {console.log(data); Alert.alert("Blood Test Results Have Successfully Been Submitted!");
                })
        }
        catch (error) {
            console.error(error);
        }
    };

    return (
        <View >
            <Text>BloodTestUpload</Text>
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Glucose Levels(mmol/L)"
                onChangeText={newText => setGlucose(newText)}
                defaultValue={glucose}
            />
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Testosterone Levels(ng/dL)"
                onChangeText={newText => setTestosterone(newText)}
                defaultValue={testosterone}
            />
            <TextInput
                style={{height: 40, padding: 5}}
                placeholder="Bile Salt Levels(mmol/L)"
                onChangeText={newText => setBileSalts(newText)}
                defaultValue={bileSalts}
            />
            <Button title = "Submit Data" onPress={sendData}/>
        </View>
    )
}