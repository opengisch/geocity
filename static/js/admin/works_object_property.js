document.addEventListener('DOMContentLoaded', function() {
  function toggleChoicesField() {
    const hiddenClass = 'grp-row-hidden';
    const requiredClass =  'required';
    const inputTypeElement = document.getElementById('id_input_type');
    const choicesElement = document.getElementById('id_choices');
    const formRowElement = choicesElement.closest('.form-row.choices');
    const labelElement = formRowElement.querySelector('label');
    const value = inputTypeElement.value;
    const visibleChoices = value === 'list_single' || value === 'list_multiple';

    if (visibleChoices) {
      formRowElement.classList.remove(hiddenClass);
      choicesElement.setAttribute('required', '');
      labelElement.classList.add(requiredClass);
    }
    else {
      formRowElement.classList.add(hiddenClass);
      choicesElement.removeAttribute('required');
      labelElement.classList.remove(requiredClass);
    }
  }

  document.getElementById('id_input_type').addEventListener('change', function(e) {
    toggleChoicesField();
  });

  toggleChoicesField();
});
