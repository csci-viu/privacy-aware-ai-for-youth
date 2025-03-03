# Load Required Packages
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("tidyr", quietly = TRUE)) install.packages("tidyr")
if (!requireNamespace("scales", quietly = TRUE)) install.packages("scales")
if (!requireNamespace("ggthemes", quietly = TRUE)) install.packages("ggthemes")

library(ggplot2)
library(tidyr)
library(scales)
library(ggthemes)

# Create Data Frame
data <- data.frame(
  Construct = c("DOC", "DOC", "DOC", "PDS", "PDS", "PRB", "PRB", "TT", "TT", "TT", "EA", "EA", "EA"),
  Item_Theme = c("Data Control Importance", "Perceived Data Control", "Comfort Data Sharing",
                 "Parental Data Sharing", "Parental Data Rights",
                 "AI Privacy Concerns", "Perceived Data Benefits",
                 "Data Usage Transparency", "Transparency Perception", "System Data Trust",
                 "Privacy Protection Knowledge", "Digital Privacy Education", "AI Privacy Awareness"),
  Youth = c(4.086, 3.351, 2.834, 2.52, 2.517, 4.093, 3.867, 4.195, 2.411, 3.093, 3.046, 2.933, 3.687),
  Educators = c(4.460, 3.405, 3.397, 2.465, 3.394, 4.252, 3.500, 4.349, 1.961, 4.079, 3.291, 2.504, 4.504),
  AI_Professionals = c(4.397, 3.644, 3.795, 1.815, 2.904, 4.315, 4.534, 4.175, 2.116, 4.185, 4.048, 3.795, 4.630)
)

# Reshape Data for ggplot using tidyr
data_melted <- pivot_longer(data, cols = c(Youth, Educators, AI_Professionals),
                            names_to = "Group", values_to = "Mean")

# Ensure Correct Order of Themes
data_melted$Item_Theme <- factor(data_melted$Item_Theme, 
                                 levels = rev(c("Data Control Importance", "Perceived Data Control", "Comfort Data Sharing",
                                                "Parental Data Sharing", "Parental Data Rights",
                                                "AI Privacy Concerns", "Perceived Data Benefits",
                                                "Data Usage Transparency", "Transparency Perception", "System Data Trust",
                                                "Privacy Protection Knowledge", "Digital Privacy Education", "AI Privacy Awareness")))

# Create the Heatmap
ggplot(data_melted, aes(x = Group, y = Item_Theme, fill = Mean)) +
  geom_tile(color = "white") + 
  scale_fill_gradientn(colors = c("darkred", "red", "orange", "yellow", "lightgreen", "darkgreen"), 
                       values = scales::rescale(data_melted$Mean), 
                       name = "Mean Score") +
  labs(title = "Stakeholder Perspectives on AI Privacy: A Heatmap Analysis", 
       x = "Stakeholder Group", 
       y = "Privacy Themes") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, vjust = 1, size = 12, face = "bold"),
        axis.text.y = element_text(size = 12),
        plot.title = element_text(hjust = 0.5, face = "bold", size = 14))
