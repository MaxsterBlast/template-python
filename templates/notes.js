// notes.js
document.addEventListener('DOMContentLoaded', function () {
   const noteInput = document.getElementById('note-input');
   const saveButton = document.getElementById('save-button');
   const noteList = document.getElementById('note-list');

   // Initialize notes as an empty array
   let notes = [];

   // Load saved notes from local storage if available
   const savedNotes = JSON.parse(localStorage.getItem('notes'));

   if (savedNotes) {
       notes = savedNotes;
       // Display saved notes
       savedNotes.forEach(function (note, index) {
           createNoteElement(note, index);
       });
   }

   // Function to create a note element
   function createNoteElement(note, index) {
       const noteDiv = document.createElement('div');
       noteDiv.textContent = note;

       const editButton = document.createElement('button');
       editButton.textContent = 'Edit';
       editButton.addEventListener('click', function () {
           const updatedNote = prompt('Edit the note:', note);
           if (updatedNote !== null) {
               notes[index] = updatedNote;
               localStorage.setItem('notes', JSON.stringify(notes));
               noteDiv.textContent = updatedNote;
           }
       });

       const deleteButton = document.createElement('button');
       deleteButton.textContent = 'Delete';
       deleteButton.addEventListener('click', function () {
           if (confirm('Are you sure you want to delete this note?')) {
               notes.splice(index, 1);
               localStorage.setItem('notes', JSON.stringify(notes));
               noteDiv.remove();
           }
       });

       noteDiv.appendChild(editButton);
       noteDiv.appendChild(deleteButton);

       noteList.appendChild(noteDiv);
   }

   // Save a new note
   saveButton.addEventListener('click', function () {
       const newNote = noteInput.value.trim();

       if (newNote !== '') {
           notes.push(newNote);
           localStorage.setItem('notes', JSON.stringify(notes));
           createNoteElement(newNote, notes.length - 1);
           noteInput.value = '';
       }
   });
});
