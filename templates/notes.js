// notes.js
document.addEventListener('DOMContentLoaded', function () {
    const noteInput = document.getElementById('note-input');
    const saveButton = document.getElementById('save-button');
    const noteList = document.getElementById('note-list');

    // Load saved notes from local storage if available
    const savedNotes = JSON.parse(localStorage.getItem('notes')) || [];

    // Display saved notes
    savedNotes.forEach(function (note) {
        const noteDiv = document.createElement('div');
        noteDiv.textContent = note;
        noteList.appendChild(noteDiv);
    });

    // Save a new note
    saveButton.addEventListener('click', function () {
        const newNote = noteInput.value.trim();

        if (newNote !== '') {
            const noteDiv = document.createElement('div');
            noteDiv.textContent = newNote;
            noteList.appendChild(noteDiv);

            // Save the note to local storage
            savedNotes.push(newNote);
            localStorage.setItem('notes', JSON.stringify(savedNotes));

            // Clear the input field
            noteInput.value = '';
        }
    });
});
