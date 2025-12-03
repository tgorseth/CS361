document.addEventListener("DOMContentLoaded", async () => {
  try {
    // Fetch user preferences (username, role, etc.)
    const prefsResponse = await fetch("http://localhost:8080/preferences/admin");
    const prefs = await prefsResponse.json();

    document.getElementById("username").textContent = `Username: ${prefs.username || "admin"}`;
    document.getElementById("role").textContent = `Role: ${prefs.role || "User"}`;

    // Fetch training progress
    const trainingsResponse = await fetch("http://localhost:8080/trainings");
    const trainings = await trainingsResponse.json();

    const trainingList = document.getElementById("trainingList");
    trainingList.innerHTML = "";

    let completedCount = 0;
    let pendingCount = 0;

    trainings.forEach(t => {
      const li = document.createElement("li");
      if (t.completed) {
        li.textContent = `${t.title} – ✅ Completed`;
        completedCount++;
      } else {
        li.textContent = `${t.title} – ⏳ Pending`;
        pendingCount++;
      }
      trainingList.appendChild(li);
    });

    document.getElementById("completed").textContent = `Completed Trainings: ${completedCount}`;
    document.getElementById("pending").textContent = `Pending Trainings: ${pendingCount}`;

  } catch (err) {
    console.error("Error fetching progress:", err);
    document.getElementById("trainingList").innerHTML = "<li>⚠️ Unable to load progress data</li>";
  }
});
