// Allow only space + Eng & length > 2
export const validateName = (name) => name.length > 2;

export const validateEmail = (email) => /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);