import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap, Normalize

linewidth=0.125

# Load an example audio file
audio_file = 'segment.mp3'
y, sr = librosa.load(audio_file)

# Separate the harmonic and percussive components
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Normalize the components for better visualization
y_harmonic_normalized = y_harmonic / np.max(np.abs(y_harmonic))
y_percussive_normalized = y_percussive / np.max(np.abs(y_percussive))

# Create a custom rainbow colormap
rainbow_cmap = LinearSegmentedColormap.from_list(
    'rainbow', ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
)

# Prepare the data for a rainbow line plot
samples_harmonic = np.arange(len(y_harmonic_normalized))
points = np.array([samples_harmonic, y_harmonic_normalized]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Create a LineCollection for the harmonic component
norm = Normalize(samples_harmonic.min(), samples_harmonic.max())
lc_harmonic = LineCollection(
    segments, cmap=rainbow_cmap, norm=norm, linewidth=linewidth, alpha=0.8
)
lc_harmonic.set_array(samples_harmonic)

# Create the figure
plt.figure(figsize=(12, 6))
ax = plt.gca()

# Add the rainbow line to the plot
ax.add_collection(lc_harmonic)

# Overlay the percussive component as a smooth, partially transparent line
plt.plot(
    samples_harmonic,
    y_percussive_normalized,
    color='gray',
    linewidth=linewidth,
    alpha=0.4,
)

# Set the axis limits
print(f'{len(samples_harmonic)}')
plt.xlim(0, len(samples_harmonic))
plt.ylim(-1.1, 1.1)

# Remove axes, labels, and decorations for a clean look
ax.axis('off')

# Save the plot with a transparent background
plt.savefig('wave.png', dpi=600, bbox_inches='tight', transparent=True)
plt.show()




