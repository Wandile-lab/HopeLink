export const saveFormData = (data) => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('draftEmergencyReport', JSON.stringify(data));
  }
};

export const loadFormData = () => {
  if (typeof window !== 'undefined') {
    const data = localStorage.getItem('draftEmergencyReport');
    return data ? JSON.parse(data) : null;
  }
  return null;
};