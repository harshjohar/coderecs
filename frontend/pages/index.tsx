import type { NextPage } from "next";
import Layout from "../components/common/Layout";
import ProblemCard from "../components/home/ProblemCard";
import ProblemListCard from "../components/home/ProblemListCard";

const problems = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}];
const problems2 = [{}, {}, {}, {}, {}];

const Home: NextPage = () => {
    return (
        <Layout>
            <div className="h-full w-full flex rounded-xl space-x-3">
                <div className="h-full w-1/2 p-3 flex flex-col space-y-3 bg-red-400 rounded-xl overflow-scroll">
                    <div className="bg-yellow-500 p-2 mx-4 mt-3">
                        <p>
                            Hello user! Lorem ipsum dolor sit amet consectetur
                            adipisicing elit. Architecto possimus iure libero
                            perferendis quidem blanditiis quo, soluta dolores
                            inventore sequi numquam optio recusandae eius
                            corporis quisquam illum eum a quae.
                        </p>
                    </div>
                    <div className="p-3 w-full flex flex-col">
                        <h1 className="text-[2.5rem] font-bold px-5">
                            Recommended Problems
                        </h1>
                        <p className="text-xs px-5">
                            Lorem ipsum dolor sit amet consectetur adipisicing
                            elit. Placeat dignissimos sint perspiciatis iusto,
                            impedit laborum necessitatibus aut autem, animi
                            corrupti eum totam amet debitis enim?
                        </p>

                        <div className="mt-5 flex flex-wrap w-full items-center justify-center">
                            {problems.map((problem) => (
                                <ProblemCard />
                            ))}
                        </div>
                    </div>
                </div>
                <div className="h-full w-1/4 bg-blue-200 py-3 flex flex-col rounded-xl">
                    <h1 className="text-xl text-center font-semibold my-2">
                        Trending problems
                    </h1>
                    <div className="space-y-3 overflow-scroll flex-1 px-3">
                        {problems.map((problem) => (
                            <ProblemListCard />
                        ))}
                    </div>
                </div>
                <div className="h-full w-1/4 rounded-xl flex flex-col justify-between">
                    <div className="bg-red-400 h-[40%] rounded-xl p-4 flex flex-col">
                        <h1 className="text-center text-xl font-semibold">
                            Problem of the Day!
                        </h1>
                        <div className="m-3 bg-yellow-500 flex-1 rounded-xl px-4 py-6 items-center flex flex-col justify-between">
                            <p className="text-lg">A. Optimal Path</p>
                            <p className="text-xs text-justify">
                                A daily problem to remind you to keep going and
                                growing. Good Luck!
                            </p>
                            <button className="bg-red-200 rounded-full p-2 hover:bg-red-400 shadow-sm">
                                Solve Now!
                            </button>
                        </div>
                    </div>
                    <div className="bg-yellow-500 h-[55%] rounded-xl p-4 flex flex-col">
                        <h1 className="text-center text-xl font-semibold">
                            Unsolved Problems
                        </h1>
                        <div className="space-y-3 overflow-scroll flex-1 px-3">
                            {problems2.map((problem) => (
                                <ProblemListCard />
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Home;
