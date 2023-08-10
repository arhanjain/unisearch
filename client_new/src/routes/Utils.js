
const BASE_URL = process.env.ENDPOINT_BASE_URL;

export const getURL = (endpoint) => {
  return BASE_URL + endpoint;
};