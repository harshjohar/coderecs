import type { NextPage } from "next";
import Layout from "../components/common/Layout";
import ProblemCard from "../components/home/ProblemCard";
import ProblemListCard from "../components/home/ProblemListCard";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import UnsolvedProblemsCard from "../components/home/UnsolvedProblemsCard";

const problems = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}];
const problems2 = [{}, {}, {}, {}, {}];

const Home: NextPage = () => {
    return (
        <Layout>
            <div className="h-full w-full flex rounded-xl space-x-3 ">
                <div className="h-full w-1/2 p-3 flex flex-col space-y-3 bg-coderecs-bgLight rounded-xl overflow-scroll scrollbar-hide shadow-[0px_0px_25px_2px_rgba(0,0,0,0.4)]">
                    <div className="p-6 mx-4 mt-3 rounded-xl text-coderecs-textDark">
                        <p>
                            Hello user! Lorem ipsum dolor sit amet consectetur
                            adipisicing elit. Architecto possimus iure libero
                            perferendis quidem blanditiis quo, soluta dolores
                            inventore sequi numquam optio recusandae eius
                            corporis quisquam illum eum a quae.
                        </p>
                    </div>
                    <div className="p-5 w-full flex flex-col">
                        <h1 className="text-[2.3rem] font-bold px-5 text-coderecs-textDark">
                            Recommended Problems
                        </h1>
                        <p className="text-xs px-5 text-coderecs-textDark">
                            Lorem ipsum dolor sit amet consectetur adipisicing
                            elit. Placeat dignissimos sint perspiciatis iusto,
                            impedit laborum necessitatibus aut autem, animi
                            corrupti eum totam amet debitis enim?
                        </p>

                        <div className="mt-5 flex flex-wrap w-full items-center justify-center scrollbar-hide">
                            {problems.map((problem) => (
                                <ProblemCard />
                            ))}
                        </div>
                    </div>
                </div>
                <div className="h-full w-1/4 py-3 flex flex-col rounded-xl shadow-[0px_0px_25px_2px_rgba(0,0,0,0.4)] bg-coderecs-bgDark">
                    <h1 className="text-xl text-center font-semibold my-2 text-coderecs-textLight">
                        Trending problems
                    </h1>
                    <div className="space-y-3 overflow-scroll flex-1 px-3 scrollbar-hide">
                        {problems.map((problem, i) => (
                            <ProblemListCard key={i} />
                        ))}
                    </div>
                </div>
                <div className="h-full w-1/4 rounded-xl flex flex-col justify-between">
                    <div className=" h-[43%] rounded-xl p-4 flex flex-col bg-coderecs-bgDark tshadow">
                        <h1 className="text-center text-xl font-semibold text-coderecs-textLight">
                            Problem of the Day!
                        </h1>
                        <div className="m-3 flex-1 rounded-xl px-4 py-5 items-center flex flex-col justify-between">
                            <p className="text-lg text-coderecs-textLight">A. Charmi and Momina Mustehasn</p>
                            <p className="text-xs text-justify text-wh text-coderecs-textLight">
                                A daily problem to remind you to keep going and
                                growing. Good Luck!
                            </p>
                            <button className="mt-6 bg-coderecs-bgLight text-coderecs-textDark hover:bg-[#145DA0] px-2 py-1.5 hover:text-white rounded-md cursor-pointer">Solve now !</button>
                        </div>
                    </div>
                    <div className="h-[55%] rounded-xl p-4 flex flex-col bg-coderecs-bgLight tshadow">
                        <h1 className="text-center text-xl font-semibold text-coderecs-textDark">
                            Unsolved Problems
                        </h1>
                        <div className="space-y-3 overflow-scroll flex-1 px-3 scrollbar-hide">
                            {problems2.map((problem, i) => (
                                <UnsolvedProblemsCard key={i}/>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Home;
