# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyArrow, Rectangle
#
# # Set up the figure and axes for the flowchart
# # fig, ax = plt.subplots(figsize=(10, 7))
# # ax.set_xlim(0, 10)
# # ax.set_ylim(0, 10)
# # ax.axis('off')
# #
# # # Define positions for flowchart elements
# # positions = {
# #     "Educators/\nParents": (1, 8),
# #     "AI\nProfessionals": (1, 6),
# #     "Young Digital\nCitizens": (1, 4),
# #     "Primary\nRisks": (5, 9),
# #     "Perceived\nBenefits": (5, 7.5),
# #     "Privacy\nConcerns": (5, 6),
# #     "Proposed\nMeasures": (5, 4.5),
# #     "Balancing\nBenefits & Privacy": (5, 3),
# #     "Ethical AI\nDevelopment": (9, 6),
# # }
# #
# # # Draw rectangles for each node
# # for label, (x, y) in positions.items():
# #     width, height = 1.8, 0.8  # Rectangle dimensions
# #     ax.add_patch(Rectangle((x - width / 2, y - height / 2), width, height,
# #                            edgecolor='black', facecolor='lightgray'))
# #     ax.text(x, y, label, fontsize=10, ha='center', va='center', wrap=True)
# #
# # # Draw arrows from groups to themes
# # groups = ["Educators/\nParents", "AI\nProfessionals", "Young Digital\nCitizens"]
# # themes = [
# #     "Primary\nRisks",
# #     "Perceived\nBenefits",
# #     "Privacy\nConcerns",
# #     "Proposed\nMeasures",
# #     "Balancing\nBenefits & Privacy",
# # ]
# #
# # for group in groups:
# #     gx, gy = positions[group]
# #     for theme in themes:
# #         tx, ty = positions[theme]
# #         ax.annotate("", xy=(tx - 0.8, ty), xytext=(gx + 0.8, gy),
# #                     arrowprops=dict(arrowstyle="->", color="gray"))
# #
# # # Draw arrows from themes to output
# # for theme in themes:
# #     tx, ty = positions[theme]
# #     ox, oy = positions["Ethical AI\nDevelopment"]
# #     ax.annotate("", xy=(ox - 0.8, oy), xytext=(tx + 0.8, ty),
# #                 arrowprops=dict(arrowstyle="->", color="gray"))
# #
# # # Title and save space by aligning closer
# # plt.title("Flowchart: Stakeholder Perspectives Leading to Ethical AI Development", fontsize=12)
# # plt.tight_layout()
# # plt.savefig("flowchart.png")
# # plt.show()
#
#
# # Adjust the flowchart with white box backgrounds and larger fonts
#
# # Adjust the flowchart with slightly larger boxes and bigger fonts for improved visibility
#
# # Adjust the flowchart with much larger boxes, less spacing, and larger fonts
#
# fig, ax = plt.subplots(figsize=(10, 7))
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# ax.axis('off')
#
# # Define positions for flowchart elements with reduced spacing
# positions = {
#     "Educators/\nParents": (1, 8.5),
#     "AI\nProfessionals": (1, 6.5),
#     "Young Digital\nCitizens": (1, 4.5),
#     "Primary\nRisks": (5, 9),
#     "Perceived\nBenefits": (5, 7.5),
#     "Privacy\nConcerns": (5, 6),
#     "Proposed\nMeasures": (5, 4.5),
#     "Balancing\nBenefits & Privacy": (5, 3),
#     "Ethical AI\nDevelopment": (9, 6),
# }
#
# # Draw larger rectangles for each node with reduced spacing
# for label, (x, y) in positions.items():
#     width, height = 2.5, 1.2  # Increased rectangle dimensions for larger text
#     ax.add_patch(Rectangle((x - width / 2, y - height / 2), width, height,
#                            edgecolor='black', facecolor='white'))
#     ax.text(x, y, label, fontsize=16, ha='center', va='center', wrap=True)  # Larger font size
#
# # Draw arrows from groups to themes
# groups = ["Educators/\nParents", "AI\nProfessionals", "Young Digital\nCitizens"]
# themes = [
#     "Primary\nRisks",
#     "Perceived\nBenefits",
#     "Privacy\nConcerns",
#     "Proposed\nMeasures",
#     "Balancing\nBenefits & Privacy",
# ]
#
# for group in groups:
#     gx, gy = positions[group]
#     for theme in themes:
#         tx, ty = positions[theme]
#         ax.annotate("", xy=(tx - 1.0, ty), xytext=(gx + 1.0, gy),
#                     arrowprops=dict(arrowstyle="->", color="gray"))
#
# # Draw arrows from themes to output
# for theme in themes:
#     tx, ty = positions[theme]
#     ox, oy = positions["Ethical AI\nDevelopment"]
#     ax.annotate("", xy=(ox - 1.0, oy), xytext=(tx + 1.0, ty),
#                 arrowprops=dict(arrowstyle="->", color="gray"))
#
# # Title and improved spacing
# plt.title("Flowchart: Stakeholder Perspectives Leading to Ethical AI Development", fontsize=18)
# plt.tight_layout()
# plt.savefig("flowchart_large_boxes.png")
# plt.show()


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import rcParams

# Set font to Times New Roman
rcParams['font.family'] = 'Times New Roman'

# Set up the figure and axes for the flowchart
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define positions for flowchart elements with reduced spacing
positions = {
    "Educators/\nParents": (1, 8.5),
    "AI\nProfessionals": (1, 6.5),
    "Young Digital\nCitizens": (1, 4.5),
    "Data Ownership\n& Control": (5, 9),
    "Parental Data\nSharing": (5, 7.5),
    "Perceived Risks\n& Benefits": (5, 6),
    "Transparency\n& Trust": (5, 4.5),
    "Education\n& Awareness": (5, 3),
    "Ethical AI\nDevelopment": (9, 6),
}

# Draw larger rectangles for each node with reduced spacing
for label, (x, y) in positions.items():
    width, height = 2.5, 1.2  # Increased rectangle dimensions for larger text
    ax.add_patch(Rectangle((x - width / 2, y - height / 2), width, height,
                           edgecolor='black', facecolor='white'))
    ax.text(x, y, label, fontsize=18, ha='center', va='center', wrap=True)  # Larger font size

# Draw arrows from groups to themes
groups = ["Educators/\nParents", "AI\nProfessionals", "Young Digital\nCitizens"]
themes = [
    "Data Ownership\n& Control",
    "Parental Data\nSharing",
    "Perceived Risks\n& Benefits",
    "Transparency\n& Trust",
    "Education\n& Awareness"
]

for group in groups:
    gx, gy = positions[group]
    for theme in themes:
        tx, ty = positions[theme]
        ax.annotate("", xy=(tx - 1.0, ty), xytext=(gx + 1.0, gy),
                    arrowprops=dict(arrowstyle="->", color="gray"))

# Draw arrows from themes to output
for theme in themes:
    tx, ty = positions[theme]
    ox, oy = positions["Ethical AI\nDevelopment"]
    ax.annotate("", xy=(ox - 1.0, oy), xytext=(tx + 1.0, ty),
                arrowprops=dict(arrowstyle="->", color="gray"))

# Title and improved spacing
plt.title("Flowchart: Stakeholder Perspectives Leading to Ethical AI Development", fontsize=20)
plt.tight_layout()
plt.savefig("flowchart_large_boxes_times_new_roman.png")
plt.show()
