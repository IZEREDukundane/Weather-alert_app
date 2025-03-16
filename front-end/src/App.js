import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomeScreen from "./screens/HomeScreen";
import AlertsScreen from "./screens/AlertsScreen";
import SettingsScreen from "./screens/SettingsScreen";
import { WeatherProvider } from "./context/WeatherContext";
import Navbar from "./components/Navbar";

function App() {
  return (
    <WeatherProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomeScreen />} />
          <Route path="/alerts" element={<AlertsScreen />} />
          <Route path="/settings" element={<SettingsScreen />} />
        </Routes>
      </Router>
    </WeatherProvider>
  );
}

export default App;
