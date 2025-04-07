import React, { useEffect, useState } from "react";
import {
  View,
  ScrollView,
  StyleSheet,
  ImageBackground,
  ActivityIndicator,
} from "react-native";
import { Text, Card } from "@rneui/themed";
import { BlurView } from "expo-blur";

interface Scores {
  symptomScore: number;
  bloodTestScore: number;
  ultrasoundScore: number;
  overallScore: number;
  recommendation: string;
  lifestyleTips: string[];
}

interface ResultsData {
  success: boolean;
  scores?: Scores;
}

export default function ResultsViewerScreen() {
  const [resultsData, setResultsData] = useState<ResultsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/getResults")
      .then((response) => response.json())
      .then((json: ResultsData) => {
        setResultsData(json);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <ImageBackground
        source={require("../assets/images/background.jpg")}
        style={styles.background}
        resizeMode="cover"
      >
        <View style={styles.center}>
          <ActivityIndicator size="large" color="#C96A86" />
          <Text style={styles.loadingText}>Loading your results...</Text>
        </View>
      </ImageBackground>
    );
  }

  if (!resultsData || !resultsData.success) {
    return (
      <ImageBackground
        source={require("../assets/images/background.jpg")}
        style={styles.background}
        resizeMode="cover"
      >
        <View style={styles.center}>
          <Text style={styles.errorText}>No results available</Text>
        </View>
      </ImageBackground>
    );
  }

  const {
    symptomScore,
    bloodTestScore,
    ultrasoundScore,
    overallScore,
    recommendation,
    lifestyleTips,
  } = resultsData.scores!;

  return (
    <ImageBackground
      source={require("../assets/images/background.jpg")}
      style={styles.background}
      resizeMode="cover"
    >
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <BlurView intensity={60} tint="dark" style={styles.blurContainer}>
          <Text h3 style={styles.title}>
            Your PCOS Scores
          </Text>

          <Card containerStyle={styles.card}>
            <Text style={styles.score}>Symptoms Score: {symptomScore}%</Text>
            <Text style={styles.score}>
              Blood Test Score: {bloodTestScore}%
            </Text>
            <Text style={styles.score}>
              Ultrasound Score: {ultrasoundScore}%
            </Text>
            <Text style={styles.overallScore}>
              Overall Score: {overallScore}%
            </Text>
          </Card>

          <Text h4 style={styles.sectionTitle}>
            Recommendation
          </Text>
          <Text style={styles.text}>{recommendation}</Text>

          <Text h4 style={styles.sectionTitle}>
            Lifestyle Tips
          </Text>
          {lifestyleTips.map((tip, idx) => (
            <Text key={idx} style={styles.text}>
              • {tip}
            </Text>
          ))}
        </BlurView>
      </ScrollView>
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
  scrollContainer: { flexGrow: 1, padding: 20 },
  center: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.4)",
  },
  blurContainer: { borderRadius: 20, padding: 20, alignItems: "center" },
  title: {
    color: "white",
    fontSize: 26,
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  card: {
    width: "100%",
    backgroundColor: "rgba(255, 255, 255, 0.1)",
    borderColor: "rgba(255,255,255,0.2)",
    borderWidth: 1,
    borderRadius: 15,
    marginVertical: 20,
  },
  score: {
    color: "#E78EA9",
    fontSize: 16,
    marginVertical: 5,
    textAlign: "center",
  },
  overallScore: {
    color: "#C96A86",
    fontSize: 18,
    fontWeight: "bold",
    marginTop: 10,
    textAlign: "center",
  },
  sectionTitle: {
    color: "#E78EA9",
    marginTop: 20,
    marginBottom: 10,
    fontWeight: "bold",
  },
  text: { color: "white", marginBottom: 5, textAlign: "center" },
  loadingText: { color: "#E78EA9", fontSize: 18, marginTop: 10 },
  errorText: { color: "#E78EA9", fontSize: 20, textAlign: "center" },
});
