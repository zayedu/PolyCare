import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';

// Define interfaces for fetched data
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
  // Type the state with ResultsData interface
  const [resultsData, setResultsData] = useState<ResultsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/getResults')
      .then(response => response.json())
      .then((json: ResultsData) => {
        setResultsData(json);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <View style={styles.container}>
        <Text style={styles.message}>Loading...</Text>
      </View>
    );
  }

  // Check if data came back empty or flagged as failure
  if (!resultsData || !resultsData.success) {
    return (
      <View style={styles.container}>
        <Text style={styles.message}>No results available</Text>
      </View>
    );
  }

  // Destructure the scores
  const {
    symptomScore,
    bloodTestScore,
    ultrasoundScore,
    overallScore,
    recommendation,
    lifestyleTips
  } = resultsData.scores!;

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Your PCOS Scores</Text>
      <Text style={styles.scoreText}>Symptoms: {symptomScore}%</Text>
      <Text style={styles.scoreText}>Blood Test: {bloodTestScore}%</Text>
      <Text style={styles.scoreText}>Ultrasound: {ultrasoundScore}%</Text>
      <Text style={styles.scoreText}>Overall: {overallScore}%</Text>

      <Text style={styles.recommendation}>{recommendation}</Text>

      <Text style={styles.tipsHeader}>Lifestyle Tips</Text>
      {lifestyleTips.map((tip: string, index: number) => (
        <Text key={index} style={styles.tipText}>
          • {tip}
        </Text>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F9E4EB', // Light Variant
    padding: 16
  },
  header: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#C96A86', // Dark Variant
    marginBottom: 16
  },
  scoreText: {
    fontSize: 16,
    marginVertical: 4,
    color: '#E78EA9' // Primary
  },
  recommendation: {
    marginTop: 20,
    fontSize: 16,
    color: '#C96A86',
    marginBottom: 10
  },
  tipsHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#C96A86',
    marginTop: 20,
    marginBottom: 8
  },
  tipText: {
    fontSize: 16,
    marginBottom: 4,
    color: '#E78EA9'
  },
  message: {
    fontSize: 18,
    color: '#C96A86'
  }
});