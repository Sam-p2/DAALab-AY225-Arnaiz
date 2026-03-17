Routing Analysis & Shortest Path Visualizer (Midterm Lab 2)
===========================================================

1\. Project Summary
-------------------

This web application is designed to evaluate and visualize routing options across a network of towns in Cavite. Through an interactive interface, users can compute the most efficient travel paths by prioritizing one of three optimization metrics: **Distance (kilometers)**, **Time (minutes)**, or **Fuel Consumption (liters)**.

2\. Execution Instructions
--------------------------

This project runs entirely on the client side as a web application, requiring no server setup or software installations.

1.  Ensure the main HTML file (e.g., MidtermLab2-Arnaiz.html) is downloaded to your local machine.
    
2.  Open the file in any modern web browser (Chrome, Edge, Firefox, etc.).
    
3.  On the left-hand control panel, select a Start Node, an End Node, and your preferred optimization metric.
    
4.  Click the "Calculate Shortest Path" button to instantly view the generated route and its highlighted path on the graph.
    

3\. Architecture & Development
------------------------------

The project was built using standard web technologies focusing on performance and a clean user experience:

*   **Graph Structure:** The provided tabular data was transformed into a directed adjacency list using native JavaScript objects, serving as the foundational data structure for the routing logic.
    
*   **Map Rendering:** The vis-network library was implemented to generate the interactive node map. Unlike static maps, this version leverages the forceAtlas2Based physics solver, allowing the nodes to dynamically adjust and letting the user drag and rearrange the network freely.
    
*   **Interface Design:** The layout was built using Tailwind CSS. It features a responsive, dual-column dashboard with a professional blue and slate color palette, cleanly separating the user controls from the graph canvas.
    

4\. Algorithmic Approach
------------------------

The core routing engine utilizes **Dijkstra's Algorithm**, which is highly effective for determining the lowest-cost path in a graph with non-negative edge weights.

Instead of writing three separate functions for distance, time, and fuel, the algorithm was optimized to accept a dynamic weight parameter. During traversal, the code accesses nested object keys based on the user's dropdown selection (graph\[currentNode\]\[neighbor\]\[criteria\]). This modular approach keeps the logic concise and highly efficient.

5\. Technical Challenges Resolved
---------------------------------

During the development phase, a few specific hurdles were addressed:

*   **Strict Directionality:** Converting the raw table data into a functional graph required careful handling of one-way versus two-way routes to ensure the directed edges strictly followed the "From" and "To" relationships.
    
*   **Visual State Management:** Translating the final array of nodes outputted by the algorithm into visual highlights on the canvas. This required matching specific IDs within the Vis.js dataset to accurately change the active route's color to yellow.
    
*   **Dynamic Cost Evaluation:** Modifying the standard Dijkstra mathematical comparisons to evaluate a variable variable string (the user's criteria) rather than a hardcoded integer value required extensive testing to ensure path accuracy didn't break during state changes.