import LoginComponent from "@/components/Login";
import Logo from "@/components/Logo";

export default function Home() {
  return (
    <div className="bg-gray-50 dark:bg-gray-900 h-screen w-screen flex justify-center items-center">
      <div className=" flex flex-col items-center justify-center">
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
          <Logo />
          <LoginComponent />
        </div>
      </div>
    </div>
  );
}
