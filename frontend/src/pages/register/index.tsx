import Logo from "@/components/Logo";
import RegisterComponent from "@/components/Register";

export default function RegisterPage() {
  return (
    <div className="bg-gray-50 dark:bg-gray-900 h-screen w-screen flex justify-center items-center">
      <div className=" flex flex-col items-center justify-center">
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
          <Logo />
          <RegisterComponent />
        </div>
      </div>
    </div>
  );
}
