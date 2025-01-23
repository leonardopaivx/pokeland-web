import { useState } from "react";
import Link from "next/link";
import { RegisterComponentI } from "@/types/LoginTypes";
import { toast } from "react-toastify";
import { fetchRegister } from "@/pages/api/api";
import { useRouter } from "next/router";

const RegisterComponent = () => {
  const [registerInfos, setRegisterInfos] = useState<RegisterComponentI>({
    username: "",
    email: "",
    password: "",
  });

  const { username, email, password } = registerInfos;
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      await fetchRegister(registerInfos);
      toast.success("Registro realizado com sucesso!");
      router.push("/");
    } catch {
      // Intencionalmente vazio
    }
  };

  return (
    <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
          Sua jornada começa aqui!
        </h1>
        <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit}>
          <div>
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              username
            </label>
            <input
              type="text"
              name="username"
              id="username"
              className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="username"
              required={true}
              value={username}
              onChange={(e) =>
                setRegisterInfos({ ...registerInfos, username: e.target.value })
              }
            />
          </div>
          <div>
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              e-mail
            </label>
            <input
              type="email"
              name="email"
              id="email"
              className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="name@company.com"
              required={false}
              value={email}
              onChange={(e) =>
                setRegisterInfos({ ...registerInfos, email: e.target.value })
              }
            />
          </div>
          <div>
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              senha
            </label>
            <input
              type="password"
              name="password"
              id="password"
              placeholder="••••••••"
              className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              required={true}
              value={password}
              onChange={(e) =>
                setRegisterInfos({ ...registerInfos, password: e.target.value })
              }
            />
          </div>
          <button
            type="submit"
            className="w-full text-gray-500 dark:text-gray-400 bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
          >
            Registrar
          </button>
          <p className="text-sm font-light text-gray-500 dark:text-gray-400">
            Já possui sua conta?{" "}
            <Link
              href="/"
              className="font-medium text-primary-600 hover:underline dark:text-primary-400"
            >
              Logar
            </Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default RegisterComponent;
