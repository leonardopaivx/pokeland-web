import { ReactNode } from "react";
import Navbar from "./Navbar";

const Layout = ({ children }: { children: ReactNode }) => {
  return (
    <div className="w-full h-full bg-gray-50 dark:bg-gray-700">
      <Navbar />
      <main className="mt-14 flex h-full w-full flex-col ">{children}</main>
    </div>
  );
};

export default Layout;
