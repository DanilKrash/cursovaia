document.querySelector('select').addEventListener('change', e => {
  const className = `${e.target.value}-info`;
  document.querySelectorAll('.fruits > div').forEach(n => {
    n.classList.toggle('visible', n.classList.contains(className));
  });
});