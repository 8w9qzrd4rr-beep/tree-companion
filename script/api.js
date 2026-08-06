export async function fetchTrees() {
    const response = await fetch('/api/v1/trees');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

export async function addTree(formData) {
  return fetch('/api/v1/add/trees', { method: 'POST', body: formData });
}

export async function signUpRequest(username, email, password){
    const formData = new FormData();
    formData.append("username", username);
    formData.append("email", email);
    formData.append("password", password);
    // Send Email for OTP
    const verified = await fetch('/api/auth/signup/otp',{
        method: 'POST',
        body: formData,
    })
    return;
}