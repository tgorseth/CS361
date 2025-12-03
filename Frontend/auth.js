document.addEventListener("DOMContentLoaded", () => {
  // LOGIN
  const loginForm = document.getElementById("loginForm");
  const loginMessage = document.getElementById("loginMessage");

  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const username = document.getElementById("username").value.trim();
      const password = document.getElementById("password").value.trim();

      try {
        const response = await fetch("http://localhost:8080/auth", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
          loginMessage.textContent = "✅ Login successful! Redirecting...";
          loginMessage.style.color = "green";
          localStorage.setItem("authToken", data.token);
          setTimeout(() => window.location.href = "dashboard.html", 1500);
        } else {
          loginMessage.textContent = `❌ ${data.detail || data.message || "Login failed"}`;
          loginMessage.style.color = "red";
        }
      } catch (err) {
        loginMessage.textContent = "⚠️ Error connecting to auth service.";
        loginMessage.style.color = "orange";
      }
    });
  }

  // CREATE USER
  const createUserForm = document.getElementById("createUserForm");
  const createMessage = document.getElementById("createMessage");

  if (createUserForm) {
    createUserForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const username = document.getElementById("newUsername").value.trim();
      const password = document.getElementById("newPassword").value.trim();
      const role = document.getElementById("role").value;

      try {
        const response = await fetch("http://localhost:8080/create-user", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, password, role })
        });

        const data = await response.json();

        if (response.ok) {
          createMessage.textContent = `✅ User "${username}" created successfully as ${role}!`;
          createMessage.style.color = "green";
        } else {
          createMessage.textContent = `❌ ${data.detail || data.message || "Failed to create user"}`;
          createMessage.style.color = "red";
        }
      } catch (err) {
        createMessage.textContent = "⚠️ Error connecting to server.";
        createMessage.style.color = "orange";
      }
    });
  }
});
