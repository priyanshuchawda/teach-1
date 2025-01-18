from pyamaze import maze, agent

m = maze(20, 10)  # 10x10 maze
m.CreateMaze()
a = agent(m, filled=True)
m.tracePath({a: m.path})
m.run()
