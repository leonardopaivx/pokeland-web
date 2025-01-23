import { LoginComponentI, RegisterComponentI } from "@/types/LoginTypes";
import axios, { AxiosRequestConfig } from "axios";
import { toast } from "react-toastify";

export const api = axios.create({
  baseURL: `${process.env.NEXT_PUBLIC_BASE_URL}`,
});

export const returnHeaders = (): AxiosRequestConfig => {
  return {
    headers: {
      "Content-Type": "application/json",
      Authorization: localStorage.getItem("token"),
    },
  };
};

api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("token");

      toast.info("Sua sessão expirou. Faça login novamente.");

      window.location.href = "/";
    }

    return Promise.reject(error);
  }
);

export const fetchRegister = async (data: RegisterComponentI) => {
  try {
    const response = await api.post("/api/v1/users", data);

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      toast.error(
        error.response?.data?.message || "Erro ao registrar o usuário."
      );
    } else {
      toast.error("Ocorreu um erro inesperado.");
    }
    throw error;
  }
};

export const fetchLogin = async (data: LoginComponentI) => {
  try {
    const response = await api.post("/api/v1/auth", data);

    const { token } = response.data;
    
    localStorage.setItem("token", token);
    toast.success("Login realizado com sucesso!");
    
  } catch (error) {
    if (axios.isAxiosError(error)) {
      toast.error(
        error.response?.data?.message || "Erro ao realizar o login."
      );
    } else {
      toast.error("Ocorreu um erro inesperado.");
    }
    throw error;
  }
};

export const fetchCatchPokemon = async () => {
  try {
    const response = await api.post("/api/v1/user-pokemons/catch", {}, returnHeaders());

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      toast.error(
        error.response?.data?.message || "Erro ao tentar capturar o Pokémon."
      );
    } else {
      toast.error("Ocorreu um erro inesperado.");
    }
    throw error;
  }
};