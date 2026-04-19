import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import SleepQuiz from "./pages/SleepQuiz";
import Results from "./pages/Results";
import NightCompanion from "./pages/NightCompanion";
import ProgressTracking from "./pages/ProgressTracking";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/quiz" element={<SleepQuiz />} />
        <Route path="/results" element={<Results />} />
        <Route path="/night-companion" element={<NightCompanion />} />
        <Route path="/progress" element={<ProgressTracking />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
