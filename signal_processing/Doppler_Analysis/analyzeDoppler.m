function info = analyzeDoppler(freqs, mag, radarFreqGHz)
%ANALYZEDOPPLER Interpret an FFT magnitude spectrum in terms of Doppler
%shift and estimated radial target speed.
%
%   info = analyzeDoppler(freqs, mag, radarFreqGHz)
%
%   freqs        - frequency bins (Hz) from computeFFT
%   mag          - magnitude at each bin
%   radarFreqGHz - radar carrier frequency in GHz (default 10.525, typical
%                  for common low-cost X-band CW Doppler modules)
%
%   info.peakFreqHz   - frequency (Hz) of the dominant spectral peak
%   info.peakMag      - magnitude at that peak
%   info.speedMps     - estimated radial speed (m/s), from f_d = 2*v*fc/c
%
% NOTE: A single-channel CW Doppler radar (like the one this project uses)
% cannot distinguish approaching vs. receding motion from magnitude alone
% (both produce a real-valued frequency after simple envelope detection);
% direction requires an I/Q ("quadrature") radar front-end, which most
% low-cost modules used here do not provide. This function reports speed
% magnitude only. See docs/Literature_Review for the direction-sensing
% upgrade path (I/Q demodulation).

    if nargin < 3
        radarFreqGHz = 10.525;
    end

    c = 3e8; % speed of light, m/s
    fc = radarFreqGHz * 1e9;

    [peakMag, idx] = max(mag);
    peakFreq = freqs(idx);

    speedMps = (peakFreq * c) / (2 * fc);

    info.peakFreqHz = peakFreq;
    info.peakMag = peakMag;
    info.speedMps = speedMps;
end
