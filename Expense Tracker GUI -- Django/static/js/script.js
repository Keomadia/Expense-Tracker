
  // JavaScript to handle the overlay display and different button actions
  const openCategoryButton = document.getElementById("addCategoryButton");
  const removeCategoryButton = document.getElementById("removeCategoryButton");
  const closeOverlay = document.getElementById("closeOverlay");
  const overlay = document.getElementById("overlay");
  const verifyButton = document.getElementById("verifyButton");
  const categoryInput = document.getElementById("categoryInput");
  const overlayTitle = document.getElementById("overlayTitle");


  function resetOverlay() {
    categoryInput.value = ""; // Clear the input field
    overlay.style.display = "none"; // Close the overlay
    document.getElementById('remheader').textContent = "";
  }

  // Open overlay for Add Category button
  openCategoryButton.addEventListener("click", function() {
    resetOverlay(); // Reset the overlay after verification
    document.getElementById('remheader').textContent = "Add New Category";
    overlay.style.display = "flex";
    verifyButton.onclick = function() {
      alert(`Category Entered: ${categoryInput.value}`);
    };
  });

  // Open overlay for Add Tag button
  removeCategoryButton.addEventListener("click", function() {
    resetOverlay(); // Reset the overlay after verification
    document.getElementById('remheader').textContent = "Remove Category";
    overlay.style.display = "flex";
    verifyButton.onclick = function() {
      alert(`Tag Entered: ${categoryInput.value}`);

    };
  });

  // Close the overlay when the X button is clicked
  closeOverlay.addEventListener("click", function() {
    document.getElementById('remheader').textContent = "";
    overlay.style.display = "none";
  });

  // Optional: Close the overlay if clicked outside the overlay content
  overlay.addEventListener("click", function(event) {
    if (event.target === overlay) {
      document.getElementById('remheader').textContent = "";
      overlay.style.display = "none";
    }
  });
